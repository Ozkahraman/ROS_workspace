// Generated by gencpp from file ogretici_paket/GorevDurumFeedback.msg
// DO NOT EDIT!


#ifndef OGRETICI_PAKET_MESSAGE_GOREVDURUMFEEDBACK_H
#define OGRETICI_PAKET_MESSAGE_GOREVDURUMFEEDBACK_H


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
struct GorevDurumFeedback_
{
  typedef GorevDurumFeedback_<ContainerAllocator> Type;

  GorevDurumFeedback_()
    : oran()  {
    }
  GorevDurumFeedback_(const ContainerAllocator& _alloc)
    : oran(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _oran_type;
  _oran_type oran;





  typedef boost::shared_ptr< ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct GorevDurumFeedback_

typedef ::ogretici_paket::GorevDurumFeedback_<std::allocator<void> > GorevDurumFeedback;

typedef boost::shared_ptr< ::ogretici_paket::GorevDurumFeedback > GorevDurumFeedbackPtr;
typedef boost::shared_ptr< ::ogretici_paket::GorevDurumFeedback const> GorevDurumFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator1> & lhs, const ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator2> & rhs)
{
  return lhs.oran == rhs.oran;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator1> & lhs, const ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ogretici_paket

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "abfa1fb1b715e7ce91c4950a3d2cbd0b";
  }

  static const char* value(const ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xabfa1fb1b715e7ceULL;
  static const uint64_t static_value2 = 0x91c4950a3d2cbd0bULL;
};

template<class ContainerAllocator>
struct DataType< ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ogretici_paket/GorevDurumFeedback";
  }

  static const char* value(const ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"string oran\n"
"\n"
;
  }

  static const char* value(const ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.oran);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GorevDurumFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ogretici_paket::GorevDurumFeedback_<ContainerAllocator>& v)
  {
    s << indent << "oran: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.oran);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OGRETICI_PAKET_MESSAGE_GOREVDURUMFEEDBACK_H