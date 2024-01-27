// Generated by gencpp from file ogretici_paket/GecenZamanResponse.msg
// DO NOT EDIT!


#ifndef OGRETICI_PAKET_MESSAGE_GECENZAMANRESPONSE_H
#define OGRETICI_PAKET_MESSAGE_GECENZAMANRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ogretici_paket
{
template <class ContainerAllocator>
struct GecenZamanResponse_
{
  typedef GecenZamanResponse_<ContainerAllocator> Type;

  GecenZamanResponse_()
    : gecen_zaman(0.0)  {
    }
  GecenZamanResponse_(const ContainerAllocator& _alloc)
    : gecen_zaman(0.0)  {
  (void)_alloc;
    }



   typedef double _gecen_zaman_type;
  _gecen_zaman_type gecen_zaman;





  typedef boost::shared_ptr< ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GecenZamanResponse_

typedef ::ogretici_paket::GecenZamanResponse_<std::allocator<void> > GecenZamanResponse;

typedef boost::shared_ptr< ::ogretici_paket::GecenZamanResponse > GecenZamanResponsePtr;
typedef boost::shared_ptr< ::ogretici_paket::GecenZamanResponse const> GecenZamanResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::ogretici_paket::GecenZamanResponse_<ContainerAllocator1> & lhs, const ::ogretici_paket::GecenZamanResponse_<ContainerAllocator2> & rhs)
{
  return lhs.gecen_zaman == rhs.gecen_zaman;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::ogretici_paket::GecenZamanResponse_<ContainerAllocator1> & lhs, const ::ogretici_paket::GecenZamanResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace ogretici_paket

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b0c3734f5b61c0954803644f9b71f2c8";
  }

  static const char* value(const ::ogretici_paket::GecenZamanResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb0c3734f5b61c095ULL;
  static const uint64_t static_value2 = 0x4803644f9b71f2c8ULL;
};

template<class ContainerAllocator>
struct DataType< ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ogretici_paket/GecenZamanResponse";
  }

  static const char* value(const ::ogretici_paket::GecenZamanResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 gecen_zaman\n"
"\n"
;
  }

  static const char* value(const ::ogretici_paket::GecenZamanResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.gecen_zaman);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GecenZamanResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ogretici_paket::GecenZamanResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ogretici_paket::GecenZamanResponse_<ContainerAllocator>& v)
  {
    s << indent << "gecen_zaman: ";
    Printer<double>::stream(s, indent + "  ", v.gecen_zaman);
  }
};

} // namespace message_operations
} // namespace ros

#endif // OGRETICI_PAKET_MESSAGE_GECENZAMANRESPONSE_H
