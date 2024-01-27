// Generated by gencpp from file ogretici_paket/GorevDurumGoal.msg
// DO NOT EDIT!


#ifndef OGRETICI_PAKET_MESSAGE_GOREVDURUMGOAL_H
#define OGRETICI_PAKET_MESSAGE_GOREVDURUMGOAL_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ogretici_paket
{
template <class ContainerAllocator>
struct GorevDurumGoal_
{
  typedef GorevDurumGoal_<ContainerAllocator> Type;

  GorevDurumGoal_()
    : birim(0)  {
    }
  GorevDurumGoal_(const ContainerAllocator& _alloc)
    : birim(0)  {
  (void)_alloc;
    }



   typedef int32_t _birim_type;
  _birim_type birim;





  typedef boost::shared_ptr< ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> const> ConstPtr;

}; // struct GorevDurumGoal_

typedef ::ogretici_paket::GorevDurumGoal_<std::allocator<void> > GorevDurumGoal;

typedef boost::shared_ptr< ::ogretici_paket::GorevDurumGoal > GorevDurumGoalPtr;
typedef boost::shared_ptr< ::ogretici_paket::GorevDurumGoal const> GorevDurumGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ogretici_paket::GorevDurumGoal_<ContainerAllocator1> & lhs, const ::ogretici_paket::GorevDurumGoal_<ContainerAllocator2> & rhs)
{
  return lhs.birim == rhs.birim;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ogretici_paket::GorevDurumGoal_<ContainerAllocator1> & lhs, const ::ogretici_paket::GorevDurumGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ogretici_paket

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4e056b4faf5ea83c15f76d58046e4e31";
  }

  static const char* value(const ::ogretici_paket::GorevDurumGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4e056b4faf5ea83cULL;
  static const uint64_t static_value2 = 0x15f76d58046e4e31ULL;
};

template<class ContainerAllocator>
struct DataType< ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ogretici_paket/GorevDurumGoal";
  }

  static const char* value(const ::ogretici_paket::GorevDurumGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"int32 birim\n"
;
  }

  static const char* value(const ::ogretici_paket::GorevDurumGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.birim);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GorevDurumGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ogretici_paket::GorevDurumGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ogretici_paket::GorevDurumGoal_<ContainerAllocator>& v)
  {
    s << indent << "birim: ";
    Printer<int32_t>::stream(s, indent + "  ", v.birim);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OGRETICI_PAKET_MESSAGE_GOREVDURUMGOAL_H